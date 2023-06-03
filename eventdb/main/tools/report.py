def counting_by(by:str, num:int):
    ws['B'+str(num)] = 'Количество событий по юридическим лицам'
    ws['B'+str(num)].font = Font(bold=True)
    entity = events.values_list(by, flat=True).distinct()
    num += 1

    for i in entity:
        ws['B'+str(num)] = i
        ws['C'+str(num)] = entity.filter(entity=i).count()
        num += 1