package com.example.demo.expose;

import com.example.demo.model.User;
import com.example.demo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class UserController {
    @Autowired
    private UserService userService;
    @GetMapping("register")
    public String showForm(Model model) {
        model.addAttribute("user", new User());
        return "register";
    }
    @PostMapping("register")
    public String registerForm(Model model, @ModelAttribute User customer,
                               BindingResult result) {
        if (result.hasErrors()) {
            return"register-confirm";
        }
        userService.add(customer);
        model.addAttribute("customers", this.userService.all());
        return "register-confirm";
    }
}
