class Robot {

    private String[] direction = {"East", "North", "West", "South"};
    private int[][] dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    private int currHeight;
    private int currWidth;
    private int dirOff;
    private int width;
    private int height;

    public Robot(int width, int height) {
        this.width = width;
        this.height = height;
        currHeight = 0;
        currHeight = 0;
        dirOff = 0;
    }
    
    public void step(int num) {
        num %= (width - 1 + height - 1) * 2;
        if (num == 0) {
            num += (width - 1 + height - 1) * 2;
        }
    
        for (int i = 0; i < num; i++) {
            int x = currWidth + dir[dirOff][0];
            int y = currHeight + dir[dirOff][1];
    
            // Check if the new position is within the bounds
            while (!(0 <= x && x < width && 0 <= y && y < height)) {
                dirOff = (dirOff + 1) % 4;
                x = currWidth + dir[dirOff][0];
                y = currHeight + dir[dirOff][1];
            }
    
            currWidth = x;
            currHeight = y;
        }
    }
    
    
    public int[] getPos() {
        return new int[]{currWidth, currHeight};
    }
    
    public String getDir() {
        return direction[dirOff];
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * Robot obj = new Robot(width, height);
 * obj.step(num);
 * int[] param_2 = obj.getPos();
 * String param_3 = obj.getDir();
 */