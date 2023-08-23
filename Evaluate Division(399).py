class Solution:
    def calcEquation(equations, values, queries):
        var = {}
        res = []
        if (len(equations) == 1):
            var[equations[0][0] + '/' + equations[0][1]] = values[0]
            var[equations[0][1] + '/' + equations[0][0]] = 1 / values[0]
            var[equations[0][0] + '/' + equations[0][0]] = 1
            var[equations[0][1] + '/' + equations[0][1]] = 1
        else:
            for i in range(len(equations)):
                for j in range(i + 1, len(equations)):
                    if (equations[i][1] == equations[j][0]):
                        var[equations[i][0] + '/' + equations[j][1]] = values[i] * values[j]
                        var[equations[j][1] + '/' + equations[i][0]] = 1 / (values[j] * values[i])
                    elif (equations[i][0] == equations[j][1]):
                        var[equations[i][1] + '/' + equations[j][0]] = values[i] * values[j]
                        var[equations[j][0] + '/' + equations[1][1]] = 1 / (values[j] * values[i])
                    elif (equations[i][1] == equations[j][1] or equations[i][0] == equations[j][0]):
                        var[equations[i][0] + '/' + equations[j][0]] = values[i] * (1 / values[j])
                        var[equations[j][0] + '/' + equations[1][0]] = (1 / values[j]) * values[i]
                if equations[i][0] + '/' + equations[i][0] not in var:
                    var[equations[i][0] + '/' + equations[i][0]] = 1
                if equations[i][1] + '/' + equations[i][1] not in var:
                    var[equations[i][1] + '/' + equations[i][1]] = 1
                var[equations[i][0] + '/' + equations[i][1]] = values[i]
                var[equations[j][0] + '/' + equations[j][1]] = values[j]
                var[equations[i][1] + '/' + equations[i][0]] = 1 / values[i]
                var[equations[j][1] + '/' + equations[j][0]] = 1 / values[j]
        for i in queries:
            if i[0] + '/' + i[1] in var:
                res.append((var[i[0] + '/' + i[1]]))
            else:
                res.append(-1.0)
        print(res)
    calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    calcEquation([["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]])