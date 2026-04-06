run("Sharpen");
setOption("BlackBackground", true);
run("Convert to Mask");
run("Despeckle");
run("Remove Outliers...", "radius=2 threshold=50 which=Dark");
