// Fill out your copyright notice in the Description page of Project Settings.

using UnrealBuildTool;
using System.Collections.Generic;

public class HauntedHeistEditorTarget : TargetRules
{
	public HauntedHeistEditorTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		DefaultBuildSettings = BuildSettingsVersion.V6;
		IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_7;
		CppStandard = CppStandardVersion.Cpp20;
		
		ExtraModuleNames.AddRange( new string[] { "HauntedHeist" } );
	}
}
