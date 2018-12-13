class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        x_max1, x_max2, x_max3 = -100, -100, -100
        x_min1, x_min2 = 100, 100
        y_max1 = -100
        y_min1, y_min2 = 100, 100
        z_min1 = 100
        for element in A:
            if float(element) >=0 and float(element) < float(2/3.0):
                current = float(element)
                if current >= x_max1:
                    x_max3 = x_max2
                    x_max2 = x_max1
                    x_max1 = current
                elif current >= x_max2:
                    x_max3 = x_max2
                    x_max2 = current
                elif current > x_max3:
                    x_max3 = current
                current = float(element)
                if current <= x_min1:
                    x_min2 = x_min1
                    x_min1 = current
                elif current < x_min2:
                    x_min2 = current
                else:
                    pass
            elif float(element) >=float(2/3.0) and float(element) <= 1:
                current = float(element)
                if current <= y_min1:
                    y_min2 = y_min1
                    y_min1 = current
                elif current < y_min2:
                    y_min2 = current
                elif current > y_max1:
                    y_max1 = current
                else:
                    pass
            elif float(element) >1 and float(element) <= 2:
                current = float(element)
                if current < z_min1:
                    z_min1 = current
            else:
                pass

        if x_max3 != -100 and x_max1 + x_max2 + x_max3 >= 1:
        	print("1")
        	return 1
        if x_min2 != 100 and  z_min1 != 100 and x_min1+x_min2+ z_min1 <= 2:
        	print("2")
        	return 1
        if x_min1 != 100 and  y_min2 != 100 and x_min1+y_min1+y_min2 <= 2:
        	print("3")
        	return 1
        if x_min1 != 100 and y_min1 != 100 and z_min1 != 100 and x_min1 +y_min1+z_min1 <= 2 and x_min1 +y_min1+z_min1 >= 1:
        	print("4")
        	return 1
        if x_max2 != -100 and y_min1 != 100 and x_max1 + x_max2 + y_min1 < 2 and x_max1 + x_max2 + y_min1 >= 1:
        	print(x_max1 ,x_max2 , y_min1)
        	print("5")
        	return 1
        if x_min2 != 100 and y_max1 != -100 and x_min1 + x_min2 + y_max1 > 1:
            return 1
        return 0

sol = Solution()
print(sol.solve([ "0.002804", "0.000298", "0.748024", "0.139023", "0.082317", "0.013348", "4.209490", "0.098512", "0.055635", "0.060427", "3.290499", "0.073212", "0.071914", "0.065654", "0.044422", "0.024968", "0.110226", "0.090197", "0.060240", "0.100432", "0.109920", "0.023673", "0.081927", "0.066987", "0.058557", "0.043674", "0.057256", "0.050478", "0.024976", "0.048124", "0.071043", "0.048199", "0.023894", "0.058934", "0.047465", "0.088664", "0.002571", "0.070546", "0.042776" ]
))

