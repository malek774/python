
function oddOccurrencesInArray(nums) {
  let result = 0;

  for (const num of nums) {
    result ^= num;
  }

  return result;
}

const nums1 = [1];
const expected1 = 1;
console.log(oddOccurrencesInArray(nums1) === expected1);

const nums2 = [5, 4, 5];
const expected2 = 4;
console.log(oddOccurrencesInArray(nums2) === expected2);

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4;
console.log(oddOccurrencesInArray(nums3) === expected3);

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;
console.log(oddOccurrencesInArray(nums4) === expected4);

