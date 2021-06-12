# M5 Forecasting Accuracy

En este repositorio se encuentra una aproximación simple de 3 diferentes técnicas diferentes a LightBGM para la predicción de la serie de tiempo. El Mayor foco se dio a el análisis de la data y su comportamiento general y específico.

Esta competencia se basa en la predicción de periodos de ventas de 28 días en base a datos históricos de ventas, eventos especiales, bonos SNAP (Supplemental Nutrition Assistance Plan) y precios de venta por producto en cada tienda. La intención de la competencia es buscar la forma donde se obtenga la mayor precisión posible en la predicción de las ventas. El método de medición a utilizar seria WRMSSE (Weighted Root Mean Scale Squared Error), esto fue decisión de los organizadores, para medirla se requiere o crear una clase personal o subir los resultados obtenidos al calificador automático proveído.

Se encontrará que hay 3 estados los cuales son California, Texas y Wisconsin, dentro de cada estado hay múltiples tiendas. Para cada una de estas tiendas tendremos las categorías de Household, Food y Hobbies. Después de este nivel vienen los departamentos por categoría, tendremos entre 1 a 3 departamentos y finalmente la cantidad de productos al final de este árbol. Tiene 4 niveles jerárquicos por encima de cada serie de tiempo y puede permitir agrupaciones para una mejor lectura de datos o incluso modelos a más alto nivel de ser requerido.

Para más información favor referirse a los documentos provistos por los organizadores para entender a profundidad el problema a solucionar y la meta deseada.

Las siguientes librerías se requieren para correr estos notebooks:

TensorFlow
FB Prophet
Matplotlib
downcast
Sklearn
Seaborn
Pandas
Tqdm

**Nota:** Tener en cuenta que el algoritmo sencillo de FB Prophet requiere un archivo Python separado para correr y hacer uso múltiples núcleos. El segundo algoritmo de FB Prophet tiene una duración superior a 24 horas de corrida.

Se recomiendan explorar la posibilidad de usar DeepAR y XGBoost para encontrar otros resultados por arboles jerárquicos.

