*** Settings ***

Library  		Collections
Library  		RequestsLibrary

*** variables ***

${ip}    192.168.5.102
${port}    47799
${server}         /webroot/decision
${HOST}           http://${ip}:${port}
&{headers}        Content-Type=application/json
${USERNAME}		Alice
${PASSWORD}		1

*** Test Cases ***

BI LOGIN
	create session  	domain		${HOST}${server}
	${data}		create dictionary	username=${USERNAME}		password=${PASSWORD}
	${response}		post request  	domain	${server}/login		headers=${headers}		data=${data}


	${resp}		to json 	 ${response.text}
	${accessToken}    Set Variable    ${resp['data']['accessToken']}
	log    ${accessToken}
	should be equal as strings  	${USERNAME}		  ${resp['data']['username']}




