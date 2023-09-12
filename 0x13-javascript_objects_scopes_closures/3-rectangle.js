#!/usr/bin/node

class Rectangle {
	constructor(w, h) {
		if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
			// Create an empty object if w or h is not a positive integer
			this.width = undefined;
			this.height = undefined;
		} else {
			// Initialize the instance attributes with the provided values
			this.width = w;
			this.height = h;
		}
	}

	print() {
		if (this.width === undefined || this.height === undefined) {
			console.log('Invalid rectangle');
		} else {
			for (let i = 0; i < this.height; i++) {
				let row = '';
				for (let j = 0; j < this.width; j++) {
					row += 'X';
				}
				console.log(row);
			}
		}
	}
}

// Example usage:
const validRectangle = new Rectangle(5, 3);
validRectangle.print();

const invalidRectangle = new Rectangle(0, 4);
invalidRectangle.print();
