"""Melting Snowman game - a word guessing game."""

# ASCII art representing the snowman melting stages (from full to melted)
SNOWMAN_STAGES = [
    # 0 hiba: Teljes hóember
    """
       _===_
      (., .)
      ( : )
     ( : : )
    """,
    # 1 hiba: Eltűnik a kalapja
    """
      (., .)
      ( : )
     ( : : )
    """,
    # 2 hiba: Eltűnik a feje (már csak a szemei/szája marad a havon)
    """
      (.. )
      ( : )
     ( : : )
    """,
    # 3 hiba: Eltűnik a felső törzse
    """
     ( : : )
    """,
    # 4 hiba: Teljesen elolvadt
    """
     _______ (Just a puddle of water!)
    """
]

def main():
    print("Welcome to Melting Snowman!")

if __name__ == "__main__":
    main()
