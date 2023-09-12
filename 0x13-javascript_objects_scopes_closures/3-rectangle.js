#!/usr/bin/node

class Rectangle {
	constructor(w, h) {
		if (
			typeof w !== 'number' ||
			typeof h !== 'number' ||
			w <= 0 ||
			h <= 0 ||
			!Number.isInteger(w) ||
			!Number.isInteger(h)
		) {
			// Create an empty object if the provided values are not valid
			return {};
		}

		this.width = w;
		this.height = h;
	}

	print() {
		for (let i = 0; i < this.height; i++) {
			console.log('X'.repeat(this.width));
		}
	}
}
module.exports = Rectangle;
