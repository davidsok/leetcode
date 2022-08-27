// Input: Fruit=['A', 'B', 'C', 'A', 'C']
// Output: 3
// Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

function fruitBasket(basket){
    let fruitMap = {}
    let windowStart = 0;
    let windowLength = 0;
    for (let windowEnd = 0; windowEnd < basket.length ; windowEnd++) {
        let rightChar = basket[windowEnd];
        if (!(rightChar in fruitMap)) {
            fruitMap[rightChar] = 0;
        }
        fruitMap[rightChar] += 1;

        while (Object.keys(fruitMap).length > 2) {
            let leftChar = basket[windowStart];
            fruitMap[leftChar] -= 1;
            if (fruitMap[leftChar] == 0){
                delete fruitMap[leftChar];
            }
            windowStart++;
        }
        windowLength = Math.max(windowLength, windowEnd - windowStart + 1)

    }

    return windowLength;
}

console.log(fruitBasket(['A', 'B', 'C', 'A', 'C']));
console.log(fruitBasket(['A', 'B', 'C', 'A','D', 'D']));