from flask import Flask, render_template, request, escape ,session 
from vsearch import search4letters
from DBcm import UseDatabase, SQLError, SqlExitError
from check_logged_in import check_logged_in

ope_path = """py -3 E:\PY_WORKSPACE\FirstPython\webapp\vsearch4web.py"""

app = Flask(__name__)

# Flask中的ap.config允许调整web应用的内部设置
app.config['dbconfig'] = {
        'host' : '192.168.5.5',
        'user' : 'root',
        'password' : '123456',
        'database' : 'vsearchlogDB1',}


def hello() -> '302':
    return redirect('/entry')


def log_request(req:'flask_request', res:str) -> None:
    
    # 使用上下文管理器
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL =  """
            insert into log(
            phrase, letters, ip, browser_string, results)
            values(%s, %s, %s, %s, %s)
            """
    cursor.execute(_SQL, (req.form['phrase'], 
                          req.form['letters'],
                          req.remote_addr, 
                          req.user_agent.browser, 
                          res,))
    


    
@app.route('/search4',methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    
    title = 'Here are you results:'
    results = str(search4letters(phrase, letters))
    
    # 处理异常
    try:
        log_request(request, results)
    except SQLError as err:
        print("****LOG ERROR*** : " + str(err))
    except SqlExitError as err:
        print('exit error is : ' + err)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
                           the_title='Welcom to search4letters on the web!')

@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    
    # 上下文管理器在数据库读日志
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, 
                        letters, ip, 
                        browser_string, 
                        results 
                    from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        
    titles = ('Phrase', 'Letters','Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
