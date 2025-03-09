function drawRace(indices, length) {
    let caracter = '~', cadena = '', salto = '';
    let espacios = ' ';
    let count = 1;
    indices.forEach((e, i) => {
        (e < 0) ? e = (length) + e : e = e;
        let renos = caracter.repeat(length);
        if(e !== 0)
            renos = renos.substring(0, e) + 'r' + renos.substring(e+1);
        (count != indices.length) ? salto = "\n" : salto = "";
        cadena += espacios.repeat((indices.length-count))+renos+' /'+count+salto;
        count += 1;
    });
    
    return cadena;
}
  
  console.log("Ejercicio #1: \n")
  console.log(drawRace([0, 5, -3], 10));
  console.log("Ejercicio #2: \n")
  console.log(drawRace([2, -1, 0, 5], 8));
  console.log("Ejercicio #3: \n")
  console.log(drawRace([3, 7, -2], 12));