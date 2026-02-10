class Student_Score:
    student_score = []

    @staticmethod
    def read_csv_file(file_path:str):
        #读取csv文件
        with open(file_path,'r',encoding='utf-8') as f:
            lines = f.readlines()       
            for line in lines:
                line = line.strip()
                line = line.split(',')
                Student_Score.student_score.append(line)

class Student_Score_calculate:
    def get_sum(self):
    #所有学生的总分
        sum_score_info = []
        for line in Student_Score.student_score[1:]:
            sum_score = []
            sum_score.append(line[0])
            sum = 0
            for student_score in line[1:]:
                sum += int(student_score)
            sum_score.append(sum) 
            sum_score_info.append(sum_score)
        return sum_score_info
    
    def get_average(self):
        #所有学生的平均分
        average_score_info = []
        for line in Student_Score.student_score[1:]:
            average_score = []
            average_score.append(line[0])
            average = 0
            for student_score in line[1:]:
                average += int(student_score)
            average_score.append(average/len(line[1:])) 
            average_score_info.append(average_score)
        return average_score_info

    def subject_avg(self):
        #计算各个科目平均分
        avg_subjects_score_info:list[list]= []
        for subject_name in Student_Score.student_score[0][1:]:     
            avg_subject_score = []
            avg_subject_score.append(subject_name)
            avg_subjects_score_info.append(avg_subject_score)
        
        subject_avg = []
        for student_score in Student_Score.student_score[1:]:
            for i in range(len(student_score[1:])):
                if len(subject_avg) < len(student_score[1:]):
                    subject_avg.append(int(student_score[1:][i]))
                else:
                    subject_avg[i] += int(student_score[1:][i])
        for i in range(len(subject_avg)):
            subject_avg[i] /=  len(Student_Score.student_score) - 1
          
                

if __name__ == "__main__":
    Student_Score.read_csv_file(".\数据分析与可视化项目\学生成绩.csv")
    print(Student_Score.student_score)
    score_calculate = Student_Score_calculate()
    score_calculate.subject_avg()