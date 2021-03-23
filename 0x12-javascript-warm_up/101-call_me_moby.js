#!/usr/bin/node
function func (x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
}