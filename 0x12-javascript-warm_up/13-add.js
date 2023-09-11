#!/usr/bin/node

function addMeMaybe(number, theFunction) {
	number++;
	theFunction(number);
}

const _addMeMaybe = addMeMaybe;
export { _addMeMaybe as addMeMaybe };
