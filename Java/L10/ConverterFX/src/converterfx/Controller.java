package converterfx;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;
import javafx.scene.control.TextFormatter;
import javafx.scene.input.KeyCode;

public class Controller {
	@FXML private TextField txt2;
	@FXML private TextField txt3;
	@FXML private TextField txt4;
	@FXML private TextField txt5;
	@FXML private TextField txt6;
	@FXML private TextField txt7;
	@FXML private TextField txt8;
	@FXML private TextField txt9;
	@FXML private TextField txt10;
	@FXML private TextField txt11;
	@FXML private TextField txt12;
	@FXML private TextField txt13;
	@FXML private TextField txt14;
	@FXML private TextField txt15;
	@FXML private TextField txt16;

	private final Map<Integer, TextField> baseFields = new HashMap<>();
	private final Map<TextField, String> preEditValue = new HashMap<>();
	private final Map<TextField, Boolean> committedSinceFocus = new HashMap<>();

	@FXML
	private void initialize() {
		baseFields.put(2, txt2);
		baseFields.put(3, txt3);
		baseFields.put(4, txt4);
		baseFields.put(5, txt5);
		baseFields.put(6, txt6);
		baseFields.put(7, txt7);
		baseFields.put(8, txt8);
		baseFields.put(9, txt9);
		baseFields.put(10, txt10);
		baseFields.put(11, txt11);
		baseFields.put(12, txt12);
		baseFields.put(13, txt13);
		baseFields.put(14, txt14);
		baseFields.put(15, txt15);
		baseFields.put(16, txt16);

		baseFields.forEach((base, field) -> {
			field.setTextFormatter(new TextFormatter<>(change -> filterChange(change, base)));

			field.focusedProperty().addListener((obs, wasFocused, isFocused) -> {
				if (isFocused) {
					preEditValue.put(field, field.getText());
					committedSinceFocus.put(field, false);
				} else {
					Boolean committed = committedSinceFocus.getOrDefault(field, false);
					if (!committed) {
						field.setText(preEditValue.getOrDefault(field, field.getText()));
					}
				}
			});

			field.setOnAction(e -> {
				committedSinceFocus.put(field, true);
				performConversionFrom(base, field.getText());
				baseFields.values().forEach(f -> preEditValue.put(f, f.getText()));
				Platform.runLater(() -> {
					field.requestFocus();
					field.positionCaret(field.getText() == null ? 0 : field.getText().length());
				});
			});

			field.setOnKeyPressed(e -> {
				if (e.getCode() == KeyCode.ENTER) {
					field.fireEvent(new javafx.event.ActionEvent());
				}
			});
		});

		performConversionFrom(10, "0");
	}

	private TextFormatter.Change filterChange(TextFormatter.Change change, int base) {
		String newText = change.getText();
		if (newText == null || newText.isEmpty()) {
			return change;
		}

		String allowed = allowedCharsForBase(base);
		StringBuilder filtered = new StringBuilder();
		for (int i = 0; i < newText.length(); i++) {
			char c = Character.toUpperCase(newText.charAt(i));
			if (allowed.indexOf(c) >= 0) {
				filtered.append(c);
			}
		}

		if (filtered.length() == 0) {
			return null;
		}

		change.setText(filtered.toString());
		return change;
	}

	private String allowedCharsForBase(int base) {
		StringBuilder sb = new StringBuilder();
		for (char d = '0'; d <= '9'; d++) {
			if (Character.digit(d, base) >= 0) sb.append(d);
		}
		for (char a = 'A'; a <= 'Z'; a++) {
			if (Character.digit(a, base) >= 0) sb.append(a);
		}
		return sb.toString();
	}

	private void performConversionFrom(int base, String valueStr) {
        if (valueStr == null || valueStr.isEmpty()) {
            baseFields.forEach((b, tf) -> tf.setText("0"));
            return;
        }

        BigInteger value = new BigInteger(valueStr, base);
        baseFields.forEach((b, tf) -> tf.setText(value.toString(b).toUpperCase()));

	}
}
