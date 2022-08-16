let paypalVal = document.querySelectorAll("#custom-price");
let payPalContainer = document.querySelectorAll("#paypal-button-container");
let payDescription = document.querySelectorAll("#pay-description");

function cleanUp(){
    const success = document.getElementById("success-wrapper")
    const error = document.getElementById("error-wrapper")
    const cancel = document.getElementById("cancel-wrapper")
    success.style.display = "none";
    error.style.display = "none";
    cancel.style.display = "none";
    return
}
function removeMessage(){

    setTimeout(() => {
    document.getElementById('message-inform').style.display = "none";
    

    }, 9000)};

for(let i = 0; i < paypalVal.length; i++){
    paypal.Buttons({

        createOrder: function(data, actions) {
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: paypalVal[i].firstChild.nodeValue.replace("$","")
                    },
                    description: payDescription[i].innerHTML
                }]
            });
        },
        onCancel: function (data) {

           cleanUp()
           document.getElementById('message-inform').style.display = "flex";
           document.getElementById('cancel-wrapper').style.display = "flex";
              removeMessage()
          },
          onError: function (err) {
        
           cleanUp()
           document.getElementById('message-inform').style.display = "flex";
           document.getElementById('cancel-wrapper').style.display = "flex";
        
        removeMessage()
          },
     
        onApprove: function(data, actions) {
            return actions.order.capture().then(function(orderData) {
                cleanUp()
                document.getElementById('message-inform').style.display = "flex";

                document.getElementById('success-wrapper').style.display = "flex";
                removeMessage()
 
            });
        }

    }).render(payPalContainer[i]);
}

































































































