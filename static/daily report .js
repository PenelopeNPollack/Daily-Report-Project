const incrementCoffeeSold = (amountSold) => {
    let coffeeSold = Number($('#coffee-sold-counter').html());
    coffeeSold += amountSold;
  
    $('#coffee-sold-counter').html(coffeeSold);
  };