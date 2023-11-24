/**
 * @param {number[]} deck
 * @return {boolean}
 */
var hasGroupsSizeX = function(deck) {
    let a = {}
    if (deck.length<2){
        return false
    }

    deck.forEach((i)=> {
        if (Object.hasOwn(a,i)){
            a[i] = ++a[i];
        }
        else {
            a[i] = 1;
        }
    });
    function gcd(a, b) 
    { 
        if (a == 0) 
            return b; 
        return gcd(b % a, a); 
    } 

    let result = Object.values(a)[0]
    for (const [key, value] of Object.entries(a)) {
        result = gcd(value, result); 
        if(result == 1) 
        { 
        return false; 
        } 
    }

    // Object.values(a).forEach((i) => {
    //     if (i!=c){
    //         return false
    //     }
    //     else{
    //         console.log(i,c)
    //     }
    // });
    return true
};