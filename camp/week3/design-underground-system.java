class UndergroundSystem {

    private Map<Integer, CheckInInfo> checkInMap = new HashMap<>();
    private Map<Route, TimeCount> timeCountMap = new HashMap<>();

    public UndergroundSystem() {
    }

    public void checkIn(int id, String stationName, int t) {
        checkInMap.put(id, new CheckInInfo(stationName, t));
    }

    public void checkOut(int id, String stationName, int t) {
        CheckInInfo checkInInfo = checkInMap.get(id);
        String startStation = checkInInfo.getStationName();
        int startTime = checkInInfo.getTime();
        Route route = new Route(startStation, stationName);

        timeCountMap.putIfAbsent(route, new TimeCount(0, 0));
        TimeCount timeCount = timeCountMap.get(route);
        timeCount.totalTime += t - startTime;
        timeCount.count++;
    }

    public double getAverageTime(String startStation, String endStation) {
        Route route = new Route(startStation, endStation);
        TimeCount timeCount = timeCountMap.get(route);

        if (timeCount != null && timeCount.count > 0) {
            return (double) timeCount.totalTime / timeCount.count;
        } else {
            return 0.0;
        }
    }

    private static class CheckInInfo {
        private String stationName;
        private int time;

        public CheckInInfo(String stationName, int time) {
            this.stationName = stationName;
            this.time = time;
        }

        public String getStationName() {
            return stationName;
        }

        public int getTime() {
            return time;
        }
    }

    private static class Route {
        private String startStation;
        private String endStation;

        public Route(String startStation, String endStation) {
            this.startStation = startStation;
            this.endStation = endStation;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Route route = (Route) obj;
            return startStation.equals(route.startStation) && endStation.equals(route.endStation);
        }

        @Override
        public int hashCode() {
            return Objects.hash(startStation, endStation);
        }
    }

    private static class TimeCount {
        private int totalTime;
        private int count;

        public TimeCount(int totalTime, int count) {
            this.totalTime = totalTime;
            this.count = count;
        }
    }
}
