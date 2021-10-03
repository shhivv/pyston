from dataclasses import dataclass
from typing import Any

@dataclass
class RunStage:
    stdout : str
    stdrr : str
    output : str
    code : int
    signal : Any

@dataclass
class CompileStage:
    stdout : str
    stdrr : str
    output : str
    code : int
    signal : Any

class Output:
    def __init__(self, json_response: dict):
        self.raw_json = json_response

        self.langauge = json_response.get("language")
        self.version = json_response.get("version")

        self.run_stage = None
        self.compile_stage = None

        runstage = json_response.get("run")
        if runstage:
            self.run_stage = RunStage(
                stdout=runstage.get("stdout"),
                stdrr=runstage.get("stdrr"),
                output=runstage.get("output"),
                code=runstage.get("code"),
                signal=runstage.get("signal")
        )

        compilestage = json_response.get("compile")
        if compilestage:
            self.compile_stage = CompileStage(
                stdout=compilestage.get("stdout"),
                stdrr=compilestage.get("stdrr"),
                output=compilestage.get("output"),
                code=compilestage.get("code"),
                signal=compilestage.get("signal")
        )

    def __repr__(self):
        return f"{self.langauge} {self.version} {self.run_stage.output}"

    def __str__(self):
        return self.run_stage.output

    @property
    def success(self) -> bool:
        return bool(self.run_stage.stdout)



class Runtime:

    def __init__(
        self,
        *,
        language,
        aliases,
        version,
        runtime
    ):
        self.language = language
        self.aliases = aliases
        self.version = version
        self.runtime = runtime

    def __str__(self) -> str:
        return self.runtime or self.language
    
    def __repr__(self) -> str:
        return  f"{self.language}-{self.version}"