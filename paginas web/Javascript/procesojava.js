 var n, numero, suma;
numero = parseInt(prompt ("ingrese un entero positivo: "));

for (let n = 1; n <=numero; n++) {
	suma = n*(n+1)/2;
	if (n==numero){
    alert(suma);
	}
}