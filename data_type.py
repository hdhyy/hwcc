import numpy as np

np.random.seed(951105)

TIME = [0]
CARDISTRIBUTION = [0, 0, 0]
CARNAMESPACE, ROADNAMESPACE, CROSSNAMESPACE = [], [], []
CROSSDICT, CARDICT, ROADDICT = {}, {}, {}


class Car(object):
    def __init__(self, id_, from_id_, to_id_, speed_, schedule_time_):
        self.id_ = id_
        self.from_id_, self.to_id_ = from_id_, to_id_
        self.speed_ = speed_
        self.schedule_time_ = schedule_time_
        self.state = 0
    #

    def __id__(self):
        return self.id_

    def __from_id__(self):
        return self.from_id_

    def __to_id__(self):
        return self.to_id_

    def __speed__(self):
        return self.speed_

    def __schedule_time__(self):
        return self.__schedule_time__


class Channel(object):
    def __init__(self, id_):
        self.id_ = id_
        self.cars_ = []

    def __cars__(self):
        return self.cars_


class Road(object):
    def __init__(self, id_, length_, speed_, channel_, from_, to_, isDuplex_):
        # **** statistic parameters ****#
        self.id_, self.length_, self.speed_, self.channel_, self.from_, \
            self.to_, self.isDuplex_ = \
            id_, length_, speed_, channel_, from_, to_, isDuplex_
        # **** dynamic parameters ****#
        self.channels_ = []

    def __from__(self):
        return self.from_

    def __to__(self):
        return self.to_

    def __length__(self):
        return self.length_

    def __channel__(self):
        return self.channel_

    def __isDuplex__(self):
        return self.isDuplex_

    def __forwardBucket__(self):
        return self.forwardBucket

    def __backwardBucket__(self):
        return self.backwardBucket


class Cross(object):
    def __init__(self, id_, north_, east_, south_, west_):
        # **** statistic parameters ****#
        self.id_ = id_
        self.roadIds = [north_, east_, south_, west_]
        self.carport = {}
        self.left = []
        # absolute loc
        self.x, self.y = 0, 0
        self.mapX, self.mapY = 0, 0
        self.cars = []
        # priorityMap
        self.directionMap = {north_: {east_: 1, south_: 2, west_: -1},
                             east_: {south_: 1, west_: 2, north_: -1},
                             south_: {west_: 1, north_: 2, east_: -1},
                             west_: {north_: 1, east_: 2, south_: -1}}
        # relationship with roads
        self.providerDirection, self.receiverDirection = [], []
        self.validRoadDirecction = []
        self.provider = [self.roadIds[direction]
                         for direction in self.providerDirection]
        self.receiver = [self.roadIds[direction]
                         for direction in self.receiverDirection]
        self.validRoad = [self.roadIds[direction]
                          for direction in self.validRoadDirecction]
        # **** flag ****#
        self.done = False

    def setDone(self, bool):
        self.done = bool

    def setLoc(self, x, y):
        self.x, self.y = x, y

    def setMapLoc(self, mapX, mapY):
        self.mapX, self.mapY = mapX, mapY

    def roadDirection(self, roadId):
        if self.roadIds[0] == roadId:
            return 0
        elif self.roadIds[1] == roadId:
            return 1
        elif self.roadIds[2] == roadId:
            return 2
        elif self.roadIds[3] == roadId:
            return 3
        else:
            return -1

    def __done__(self):
        return self.done

    def __cars__(self):
        return self.cars

    def __loc__(self):
        return self.x, self.y

    def __mapLoc__(self):
        return self.mapX, self.mapY

    def __validRoad__(self):
        return self.validRoad
