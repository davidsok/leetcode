function smallest_subarray_sum(s, arr){
    let window_start = 0;
    let window_sum = 0;
    let window_length = Infinity;

    for (let window_end = 0; window_end < arr.length; window_end++){
        window_sum += arr[window_end];
        while ( window_sum >= s ){
            window_length = Math.min(window_length, window_end - window_start + 1);
            window_sum -= arr[window_start];
            window_start++;
        }
    }
    return window_length;
}


console.log(`Smallest subarray length: ` + smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2]));
console.log(`Smallest subarray length: ` + smallest_subarray_sum(7, [2, 1, 5, 2, 8]));
console.log(`Smallest subarray length: ` + smallest_subarray_sum(8, [3, 4, 1, 1, 6]));