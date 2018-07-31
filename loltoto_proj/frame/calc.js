function getMatch(_participants){
    return int(_participants / 2);
}

function getAwardList(_participants, _initial, _magni){
    var multi = [];
    var p = _participants;
    var tmp = p - 1;
    var r = _initial;
    while (p > 1){
        for (var i = 0; i < getMatch(p); i++){
            multi.push([r, tmp]);
            tmp -= 1;
        }
        p = p - getMatch(p);
        r *= magni;
    }
    return multi;
}

function getMultiList(_participants){
    var multi = [];
    var p = _participants;
    var tmp = p - 1;
    var r = 1;
    while (p > 1){
        for (var i = 0; i < getMatch(p); i++){
            multi.push([r, tmp]);
            tmp -= 1;
        }
        p = p - getMatch(p);
        r += 1;
    }
    return multi;
}