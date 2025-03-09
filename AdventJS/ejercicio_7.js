function fixPackages(packages) {
    if(packages.length == 0)
      return '';
      
    var lista_tmp = [], letras = [], tmp ='';
    packages.split('').forEach(e => {
        lista_tmp.push(e);
      if(lista_tmp.includes('(') && e == '(')
          lista_tmp = [];
      else if(lista_tmp.length > 1 && e == ')'){
          letras = lista_tmp.slice(0, -1).reverse().join('');
          tmp = '('+lista_tmp.join('');
          packages = packages.replace(tmp, letras);
      }
    });
    
    
    if(packages.includes('('))
        return fixPackages(packages);

    return packages;
    
  }