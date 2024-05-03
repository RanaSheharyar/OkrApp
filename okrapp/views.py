from django.shortcuts import render
from django.http import JsonResponse
from .models import Checklist, KJBGoalType, KJBCategory, CategoryPoints

def sub_categories(request, checklist_name):
    data = {}

    # Get the KJBGoalType based on the checklist name
    try:
        kjb_goal_type = KJBGoalType.objects.get(name=checklist_name)
    except KJBGoalType.DoesNotExist:
        return JsonResponse({'error': f'Checklist "{checklist_name}" not found'})

    # Get all KJBGoals associated with the KJBGoalType
    kjb_goals = KJBGoal.objects.filter(goal_type=kjb_goal_type)

    sub_categories = []

    # Iterate over each KJBGoal to fetch associated sub-categories
    for kjb_goal in kjb_goals:
        # Get the KJBCategory associated with the KJBGoal
        kjb_category = kjb_goal.kjb_category_id

        # Get all sub-categories associated with the KJBCategory
        category_points = CategoryPoints.objects.filter(category=kjb_category)

        # Append sub-category names to the list
        sub_categories.extend(category_points.values_list('name', flat=True))

    # Remove duplicates
    sub_categories = list(set(sub_categories))

    # Add sub-categories to the response data
    data['sub_categories'] = sub_categories

    return JsonResponse(data)
