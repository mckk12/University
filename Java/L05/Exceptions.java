class GraException extends Exception {
    public GraException(String message) { super(message); }
    public GraException(String message, Throwable cause) { super(message, cause); }
}

// Gdy wpisany ciąg nie jest poprawną liczbą
class InvalidFormatException extends GraException {
    public InvalidFormatException(String message) { super(message); }
}

/** Gdy liczba poza zakresem (0, 1) */
class ValueOutOfRangeException extends GraException {
    public ValueOutOfRangeException(String message) { super(message); }
}

/** Gdy mianownik jest większy niż dopuszczalny maksimum. */
class DenominatorTooLargeException extends GraException {
    public DenominatorTooLargeException(String message) { super(message); }
}

