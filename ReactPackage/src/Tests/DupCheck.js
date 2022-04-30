const hasDuplicate = (arrayObj, colName) => {
    var hash = Object.create(null);
    return arrayObj.some((arr) => {
       return arr[colName] && (hash[arr[colName]] || !(hash[arr[colName]] = true));
    });
 };
 var isDuplicate = hasDuplicate(posts, "rental_name");
 console.log(isDuplicate);