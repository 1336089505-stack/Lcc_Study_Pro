def process_logs(file_path):
    """
    数据分类：
    正常类：解析出 (传感器ID, 数值) 并存入列表。
    报警类：如果包含 ALERT 关键字，将其存入另一个专门的“报警记录”列表。
    :param file_path:
    :return:
    """
    #处理重复后数据
    logs_list = []
    #剔除的重复数据
    logs_repeat_list = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            check = True
            if not logs_list:
                logs_list.append(line.strip())
            else:
                for logs in logs_list:
                    if logs == line.strip():
                        check = False
                        break
            if check:
                logs_list.append(line.strip())
            else:
                logs_repeat_list.append(line.strip())

    #正常类
    normal_logs_list = []
    #报警类
    alarm_logs_list = []
    for logs in logs_list:
        if "ALERT" in logs:
            logs_tmp = logs.split(",")
            alarm_logs_list.append(logs_tmp)
        elif "INFO" in logs:
            continue
        else:
            logs_tmp = logs.split(",")
            nor_tmp = logs_tmp[0]+","+logs_tmp[2]
            normal_logs_list.append(nor_tmp)
    return normal_logs_list, alarm_logs_list, logs_list,logs_repeat_list

def analyze_alerts(alert_list):
    """
    统计：计算每个传感器触发 ALERT 的次数。
    平均值：计算所有报警状态下的平均数值。
    :param alert_list:
    :return:
    """
    #传感器触发 ALERT 的次数
    alert_num_dict = {}
    sum_alerts = 0
    for alert in alert_list:
        if alert[0] not in alert_num_dict:
            alert_num_dict[alert[0]] = 1
        else:
            alert_num_dict[alert[0]] += 1
        sum_alerts += float(alert[2])
    #所有报警状态下的平均数值
    average = sum_alerts / len(alert_list)
    return sorted(alert_num_dict),alert_num_dict

def export_audit(normal_data, alert_summary, output_file = ''):
    """
    编写审计报告函数export_audit(normal_data, alert_summary, output_file)，完成格式化输出：
    (1)第一部分：列出总处理行数、剔除的重复行数。
    (2)第二部分：按传感器 ID 升序排列，输出正常数据的平均值。
    (3)第三部分：危险名单。列出触发 ALERT 次数超过 5 次的传感器 ID。
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines("--------第一部分-------\n")
        f.writelines(f"------1.总处理行数:{len(normal_data[0])}------\n")
        """
        for normal in normal_data[0]:
            f.writelines(normal+"\n")
            """
        f.writelines(f"------2.剔除的重复行数:{len(normal_data[1])}------\n")
        """
        for normal in normal_data[1]:
            f.writelines(normal + "\n")
            """
        f.writelines("--------第二部分-------\n")
        normal_average_dict = {}
        normal_num_dict = {}
        for normal in normal_data[3]:
            normal_tmp = normal.split(",")
            if normal_tmp[0] not in normal_average_dict:
                normal_average_dict[normal_tmp[0]] = float(normal_tmp[1])
            else:
                normal_average_dict[normal_tmp[0]] += float(normal_tmp[1])

            if normal_tmp[0] not in normal_num_dict:
                normal_num_dict[normal_tmp[0]] = 1
            else:
                normal_num_dict[normal_tmp[0]] +=1
        for normal in normal_data[2]:
            f.writelines(normal + "平均值:"+f"{round(normal_average_dict[normal]/normal_num_dict[normal],2)}" + "\n")
        f.writelines("--------第三部分-------\n")
        for alert in alert_summary:
            if alert_summary[alert] > 5:
                f.writelines(f"{alert}传感器触发 ALERT 次数： {alert_summary[alert]}次\n")

if __name__ == '__main__':
    a = process_logs('./raw_logs.txt')
    b = analyze_alerts(a[1])
    tmp = [a[2],a[3],b[0],a[0]]
    export_audit(tmp,b[1],'./out_put.txt')

