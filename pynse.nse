local nmap = require "nmap"
local standardnse = require "stdnse"
local shortport = require "shortport"

description = [[
    pynse
]]

author = "Mike Felch - @ustayready"
portrule = shortport.http

action = function(host, port)
    local ip = host.ip
    local portnumber = port.number
    local plugin = standardnse.get_script_args("plugin")
    local cmd = "pynse --host " .. ip .." --port " .. portnumber .. " --plugin " .. plugin
    local ret = os.execute(cmd)

    if ret then
        result = "Successfully ran " .. plugin
    end

    return standardnse.format_output(true, result)
end
