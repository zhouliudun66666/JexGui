import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.io.File;

public class test {
    public WebDriver driver;

    @BeforeClass
    public void beforMethod(){
        File file=new File("E:\\GUI\\chromedriver.exe");
        System.setProperty("webdriver.chrome.driver", file.getAbsolutePath());
        System.out.println("驱动");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("http://test.coinfex.com/");
    }
    @Test
    public void main() throws InterruptedException {
        driver.navigate().to("http://test.coinfex.com/");
        Thread.sleep(8);
        driver.findElement(By.xpath("//*[@id=\"header\"]/div[2]/div[3]/div[1]/div[1]/a/div")).click();
        Thread.sleep(500);
        driver.findElement(By.xpath("//*[@id=\"login-main\"]/div[2]/div[1]/input[1]")).sendKeys("13900000190");
        Thread.sleep(500);
        driver.findElement(By.xpath("//*[@id=\"login-main\"]/div[2]/div[1]/input[2]")).sendKeys("123456");
        Thread.sleep(300);
        driver.findElement(By.xpath("//*[@id=\"login-main\"]/div[2]/div[2]/div[1]/button")).click();
        //获取登录用户
        Thread.sleep(3000);
        WebElement username = driver.findElement(By.xpath("//*[@id=\"header\"]/div[2]/div[3]/div[2]/div"));
        String value = username.getAttribute("textContent");
        System.out.println(value);
        String accont = "139****0190";
        //String accont1 = "139****0191";
        Assert.assertEquals(value,accont,"断言值成功");
    }

    @AfterClass
    public void afterMethod() {
        driver.quit();
    }
}
