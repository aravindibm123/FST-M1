public class implictwaitDemo {
    public static void main(string args[]) {
        system.setproperty(FireFoxDriver.systemproperty.Browser_Logfile, "/dev/null");
        webDriverManager.firefoxDriver().setup();
        WebDriver driver = new FirefoxDriver();
        driver.manager().timeout().implictlywait(Duration.of selenium(20));
        driver.get(" https://v1.training-support.net/");
        // find  the heading
        WebElement h = driver.findElement(By.tagname("h1"));
        //Get the text
        String text = h.getText();
        //print the text
        System.out.println(text);
        driver.quit();
    }
}
