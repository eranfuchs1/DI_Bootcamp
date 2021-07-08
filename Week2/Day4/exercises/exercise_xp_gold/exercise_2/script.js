let abbrevName = (name) => name.replaceAll(/(?<!^\w{1,})(?!\b)[\w]{1,}$/g,'.');
console.log(abbrevName('Lorem Ipsum Sum Ddff'));
