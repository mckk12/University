package converterfx;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("converterfx.fxml"));
        Parent root = loader.load();
        Scene scene = new Scene(root);

        String css = getClass().getResource("styles.css").toExternalForm();
        scene.getStylesheets().add(css);

        stage.setTitle("ConverterFX");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
