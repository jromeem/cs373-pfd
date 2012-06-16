console.log("51 50");

for (i = 51; i > 0; i--){
	tworand = false;
	rand1 = Math.ceil(Math.random()*i);
	while (rand1 >= i){
		if (i == 1){
			rand1 = 0;
			break;
		}
		else
			rand1 = Math.ceil(Math.random()*50);
	}
	
	if (Math.random() >= .5){
		tworand = true;
		rand2 = Math.ceil(Math.random()*i);
		while (rand2 >= i || rand2 == rand1){
			if (i == 1){
				rand2 = 0;
				break;
			}
			else
				rand2 = Math.ceil(Math.random()*50);
		} 
	}
	
	if (i != 1){
		if (tworand)
			console.log(i + " 2 " + rand1 + " " + rand2);
		else
			console.log(i + " 1 " + rand1);
	}
}
