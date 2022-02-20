/* 2 question 12 sprint */
    
const product = function() {
    return [].reduce.call(arguments, function(res, elem) {
      return res * elem;
    }, this.product);
};

const contextObj = {product: 10};

const getProduct = product.bind(contextObj, 2, 3);

console.log(getProduct(4, 5)); //1200

