
function compile(instructions) {
    if(instructions.length == 0)
        return 0

    let indices = []
    let codigo = 'A'.charCodeAt(0);
    let posiciones = ['A', 'B', 'C', 'D'];
    let indx1 = 0;
    for(var i = 0; i < 4; i++){
        indices[i] = [String.fromCharCode(codigo), 0];
        codigo += 1;
    }
      for(let i = 0; i < instructions.length; i++){
        let e = instructions[i].trim().split(' ');
        let idx1 = posiciones.indexOf(e[1]);
        let idx2 = posiciones.indexOf(e[2]);
        if(e[0] == 'MOV' && !isNaN(e[1]) && idx2 !== -1 ){
          indices[idx2][1] = parseInt(e[1]);
          break;
        }else if(e[0] == 'MOV' && isNaN(e[1]) && isNaN(e[2]) && idx1 !== -1 && idx2 !== -1){
          indices[idx2][1] = indices[idx1][1];
          break;
        }else if(e[0] == 'INC' && isNaN(e[1]) && idx1 !== -1){
          indices[idx1][1] += 1;
          break;
        }else if(e[0] == 'DEC' && isNaN(e[1]) && idx1 !== -1){
          indices[idx1][1] -= 1;
          break;
        }else if(e[0] == 'JMP' && isNaN(e[1]) && !isNaN(e[2]) && idx1 !== -1 && indices[idx1][1] === 0){
            i = parseInt(e[2]);
            break;
        }
      }

      return (indices[0][1] == 0) ? undefined : parseInt(indices[0][1]);
}

let instructions = [ 'MOV -1 C ', 'INC C', 'JMP C 1', 'MOV C A', 'INC A'];

console.log(compile(instructions))