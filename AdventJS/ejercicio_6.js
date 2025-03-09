function inBox(box){
    box.forEach(subarray => {
        if (subarray[0] == '*' || subarray[subarray.length()-1] == '*'){
            return false
        }
    });

    var box_plano = box.flat();
    if(box_plano.includes('*')){
        return true;
    }else{
        return false;
    }
}

// Primer ejercicio con js

function prepareGifts(gifts) {
    gifts = gifts.filter((valor, arreglo, index) => {
        return arreglo.index(valor) === index
    })
}

gifts = [1,2,3,7,7,8,9,9,0,1];
console.log(prepareGifts(gifts))
