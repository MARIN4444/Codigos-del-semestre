var pan, pan_no_dia, descuento, pan_vendido, valor_total;
pan_vendido = parseInt(prompt("ingrese cuantas barras de pan que no es del dia vendio: "));
pan = 4500;
descuento = 4500*0.6;
pan_no_dia = pan-descuento;
valor_total = pan_no_dia*pan_vendido;

document.write("precio habitual de una barra de pan: $", pan +"<br>")
document.write("descuento que se le hace por no ser del dia: $", descuento +"<br>")
document.write("valor total del pan que no es del dia: $",valor_total )
