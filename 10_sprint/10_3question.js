/* 3 question 10 sprint */


function longestLogin(loginList) {
    function reducer(total, value) {
        if (total.length <= value.length){
            total = value}
        return total;
    }
    const login = loginList.reduce(reducer);
    return login;
}


// longestLogin(["serg22", "tester_2", "Prokopenko", "guest"]);   //  Prokopenko

// longestLogin(["user1", "user2", "333", "user4", "aa"]);   //  user4


