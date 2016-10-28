var SESSION;

/**
 * Autobahn
 */
function bind_autobahn()
{
    // the URL of the WAMP Router (Crossbar.io)
    var wsuri = WSURI;
    var connection = new autobahn.Connection({
        url: wsuri,
        realm: "realm1"
    });
    // fired when connection is established and session attached
    //
    connection.onopen = function (session, details) {
        console.log("Connected");
        // saves the session globally for later
        SESSION = session;
    };
    // fired when connection was lost (or could not be established)
    //
    connection.onclose = function (reason, details) {
        console.log("Connection lost: " + reason);
    }
    // now actually open the connection
    //
    connection.open();
}

/**
 * RPC call to the backend servo_move() method.
 */
function rpc_servo_move(session, servo_num, servo_pos, servo_speed)
{

    session.call('io.github.andremiras.servo_move', [servo_num, servo_pos, servo_speed]).then(
        function (res) {
            // console.log("servo_move() result:", res);
        },
        function (err) {
            console.log("servo_move() error:", err);
        }
    );
}

/**
 * Binds slider value (change event) with the rpc_servo_move().
 */
function bind_slider()
{
  var slider_elem = $("input.slider");
  var options = {
  };
  slider_elem.slider(options);

  slider_elem.on("change", function(slideEvt) {
    var servo_num = SERVO_NUM;
    var servo_pos = slideEvt.value.newValue;
    var servo_speed = SERVO_SPEED;
    // console.log("slide: " + servo_pos);
    rpc_servo_move(SESSION, servo_num, servo_pos, servo_speed);
  });
}
