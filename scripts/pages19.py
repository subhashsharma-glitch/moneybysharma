# "The $24 magic money tree" (power of compounding) article, exec'd from build.py after pages18.
# The article body is kept verbatim in scripts/content/power-of-compounding.body.html (from /workspace/out/power-of-compounding/);
# edit content there, not in the generated power-of-compounding.html. Figures live in assets/compounding/, PDF in assets/downloads/.
import html as _h
pages["power-of-compounding.html"] = page("power-of-compounding.html", 'The power of compounding: the $24 magic money tree – MoneyBySharma',
 _h.unescape('Compounding explained simply: how $24 for Manhattan could have grown to $13.6 trillion at 7% a year, the doubling trick, Arjun and Saachi, and what breaks the magic. Information, not advice.'), open("scripts/content/power-of-compounding.body.html").read())
