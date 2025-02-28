function createFs(n) { // tworzy tablicę n funkcji
    var fs = []; // i-ta funkcja z tablicy ma zwrócić i
    for (var i=0; i<n; i++ ) {          //var jest globalna dlatego kazde wywolanie 'i' w petli odwoluje sie to tej samej zmiennej ze skonczonej petli
        fs[i] = (function (i) {         //bierze 'i' jako argumetn i zwraca nowa funkcje ktora zwraca przechwycone 'i' dla danej iteracji
            return function () {
              return i;
            };
          })(i);
    };

    return fs;
}

var myfs = createFs(10);

console.log( myfs[0]() ); // zerowa funkcja miała zwrócić 0
console.log( myfs[2]() ); // druga miała zwrócić 2
console.log( myfs[7]() );
// 10 10 10               // ale wszystkie zwracają 10?

