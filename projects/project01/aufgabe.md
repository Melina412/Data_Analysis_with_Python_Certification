Erstelle eine Funktion namens calculate() in mean_var_std.py, die Numpy benutzt, um den Mittelwert, die Varianz, die Standardabweichung, Max, Min, und die Summe der Zeilen, Spalten und Elemente in einer 3 x 3 Matrix anzugeben.

Die Eingabe der Funktion sollte eine Liste mit 9 Ziffern sein. Die Funktion sollte die Liste in ein 3 x 3 Numpy Array konvertieren und dann ein Wörterbuch mit dem Mittelwert, der Varianz, der Standardabweichung, Max, Min, sowie die Summe entlang beider Achsen und für die abgeflachte Matrix zurückgeben.

Das zurückgegebene Wörterbuch sollte diesem Format folgen:

```py
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

Wenn eine Liste mit weniger als 9 Elementen an die Funktion übergeben wird, sollte eine ValueError-Ausnahme mit der Nachricht "Liste muss neun Nummern enthalten." auftauchen. Die Werte im zurückgegebenen Wörterbuch sollten Listen und keine Numpy Arrays sein.

Zum Beispiel sollte calculate([0,1,2,3,4,5,6,7,8]) zurückgeben:

```py
{
 'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
 'max': [[6, 7, 8], [2, 5, 8], 8],
 'min': [[0, 1, 2], [0, 3, 6], 0],
 'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```
