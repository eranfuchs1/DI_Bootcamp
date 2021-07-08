let str = '';
let display_str = '';
let answer;
let display_result = (dis) => {
	answerElem = document.getElementById('answer');
	answerElem.innerHTML = dis;
}
let number = (num) => {
	str += num;
	display_str += num;
	display_result(display_str);
}
let operator = (opr) => {
	str += opr;
	display_str += opr;
	display_result(display_str);
}
let equal = () => {
	if (str.length > 0)
	{
		if (/^[0-9]*\;[0-9]{1,}/.test(str))
		{
			str = str.replace(/^[0-9]{1,}[\;]{1}]/, '');
		}
		else if (str.match(/\;/)){
			str = str.replace(/\;{1}/,'');
			console.log('replacing');
		}
		if (str.match(/[0-9]$/))
		{
			answer = eval(str);
			display_result(answer);
			str = `${answer};`;
			display_str = `${answer}`;
		}
	}
}
let clear_scr = () => {
	display_result('');
}
let reset = () => {
	str = '';
	display_str = '';
	clear_scr();
}
let backspace = () => {
	str = str.match(/\;/) ?  str.replace(/.;/, ';') : str.replace(/.$/, '');
	display_str = display_str.replace(/.$/, '');
	display_result(display_str);
}
