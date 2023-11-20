function findCommonElements(lista)
{
    let com = lista[0];
    return lista.reduce((a,b)=> commons(a,b), com);    
}

function commons(lista1, lista2)
{
    return lista1.filter(x => lista2.includes(x));    
} 