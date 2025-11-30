# src/converter.py

def m_to_cm(metre: float) -> float:
    """Metreyi santimetreye çevirir."""
    return metre * 100

def cm_to_m(cm: float) -> float:
    """Santimetreyi metreye çevirir."""
    return cm / 100

if __name__ == "__main__":
    # Küçük bir test çıktısı
    print("5 metre =", m_to_cm(5), "cm")
    print("250 cm =", cm_to_m(250), "m")