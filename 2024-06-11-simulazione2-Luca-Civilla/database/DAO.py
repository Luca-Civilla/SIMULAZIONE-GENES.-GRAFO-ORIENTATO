from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getCromosomi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select g.Chromosome 
                from genes g 
                where g.Chromosome !=0"""

        cursor.execute(query, )

        for row in cursor:
            result.append(row["Chromosome"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(u,v):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct g1.Chromosome as cromosone1, g2.Chromosome as cromosone2, g1.GeneID as gene1, g2.GeneID as gene2, i.Expression_Corr 
                from genes g1, genes g2, interactions i  
                where g1.Chromosome =%s and g2.Chromosome =%s and i.GeneID1 = g1.GeneID and i.GeneID2 = g2.GeneID
                """

        cursor.execute(query,(u,v,) )

        for row in cursor:
            result.append((row["cromosone1"],row["cromosone2"],row["gene1"],row["gene2"],row["Expression_Corr"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(u,v):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select sum(distinct i.Expression_Corr) as totale 
                from genes g1, genes g2, interactions i  
                where g1.Chromosome =%s and g2.Chromosome =%s and i.GeneID1 = g1.GeneID and i.GeneID2 = g2.GeneID"""

        cursor.execute(query,(u,v,) )

        for row in cursor:
            result.append(row["totale"])

        cursor.close()
        conn.close()
        return result