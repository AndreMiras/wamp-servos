from __future__ import unicode_literals
from os import environ
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from libcontroller import serial_conf, move_one


class Component(ApplicationSession):
    """
    An application component providing procedures with different kinds
    of arguments.
    """

    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")
        self.serial = None

        def servo_move(servo_num, servo_pos, servo_speed):
            if self.serial is None:
                self.serial = serial_conf()
            move_one(self.serial, servo_num, servo_pos, servo_speed)

        yield self.register(servo_move, 'io.github.andremiras.servo_move')
        print("Procedures registered; ready for frontend.")


if __name__ == '__main__':
    router_address = environ.get(
        "AUTOBAHN_DEMO_ROUTER", "ws://127.0.0.1:8080/ws")
    runner = ApplicationRunner(
        unicode(router_address),
        "realm1",
    )
    runner.run(Component)
